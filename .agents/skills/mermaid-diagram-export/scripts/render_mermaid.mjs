#!/usr/bin/env node
/** Render stdin Mermaid through loopback HTTP (no file:// browser access). */
import { createServer } from 'node:http';
import { readFile, realpath, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import puppeteer from 'puppeteer';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../../..');
let browser;
let server;

try {
  const options = {};
  const allowed = new Set(['--output', '--format', '--puppeteer-config']);
  const args = process.argv.slice(2);
  for (let i = 0; i < args.length; i += 2) {
    if (!allowed.has(args[i]) || !args[i + 1]) throw new Error('Expected --output ABS --format svg|png --puppeteer-config JSON');
    options[args[i]] = args[i + 1];
  }
  if (!path.isAbsolute(options['--output'] ?? '') || !['svg', 'png'].includes(options['--format']) || !options['--puppeteer-config']) {
    throw new Error('Expected --output ABS --format svg|png --puppeteer-config JSON');
  }
  let source = '';
  process.stdin.setEncoding('utf8');
  for await (const chunk of process.stdin) source += chunk;
  if (!source.trim()) throw new Error('Mermaid source on stdin is empty');

  const moduleRoot = await realpath(path.join(root, 'node_modules'));
  const html = `<!doctype html><html><head><meta charset="utf-8"></head><body style="margin:0;background:white"><div id="diagram"></div><script type="module">
    import mermaid from '/node_modules/mermaid/dist/mermaid.esm.min.mjs';
    import elk from '/node_modules/@mermaid-js/layout-elk/dist/mermaid-layout-elk.esm.min.mjs';
    mermaid.registerLayoutLoaders(elk);
    mermaid.initialize({startOnLoad:false});
    window.renderDiagram = async (source) => {
      const {svg} = await mermaid.render('fde-diagram', source);
      const container = document.querySelector('#diagram');
      container.innerHTML = svg;
      await document.fonts.ready;
      await Promise.all([...container.querySelectorAll('image')].map(element => new Promise((resolve,reject) => {
        const image = new Image();
        image.onload = resolve;
        image.onerror = () => reject(new Error('Unable to load diagram image'));
        image.src = element.getAttribute('href') || element.getAttribute('xlink:href');
      })));
      const element = container.querySelector('svg');
      const box = element.viewBox.baseVal;
      if (!(box.width > 0 && box.height > 0)) throw new Error('Diagram has no positive native viewBox');
      container.style.width = box.width + 'px';
      container.style.height = box.height + 'px';
      await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
      return {svg, width:Math.ceil(box.width), height:Math.ceil(box.height)};
    };
  </script></body></html>`;
  server = createServer(async (request, response) => {
    try {
      if (request.method !== 'GET') { response.writeHead(405).end(); return; }
      const pathname = decodeURIComponent(new URL(request.url, 'http://localhost').pathname);
      if (pathname === '/') { response.writeHead(200, {'Content-Type':'text/html; charset=utf-8'}).end(html); return; }
      if (!pathname.startsWith('/node_modules/')) { response.writeHead(404).end(); return; }
      const candidate = path.resolve(moduleRoot, pathname.slice('/node_modules/'.length));
      const inside = target => target.startsWith(moduleRoot + path.sep);
      if (!inside(candidate)) { response.writeHead(403).end(); return; }
      const resolved = await realpath(candidate);
      if (!inside(resolved)) { response.writeHead(403).end(); return; }
      const data = await readFile(resolved);
      const type = /\.(mjs|js)$/.test(resolved) ? 'text/javascript' : resolved.endsWith('.json') ? 'application/json' : 'application/octet-stream';
      response.writeHead(200, {'Content-Type':type, 'X-Content-Type-Options':'nosniff'}).end(data);
    } catch {
      response.writeHead(404).end();
    }
  });
  await new Promise((resolve, reject) => { server.once('error', reject); server.listen(0, '127.0.0.1', resolve); });
  const config = JSON.parse(await readFile(options['--puppeteer-config'], 'utf8'));
  if (process.env.PUPPETEER_EXECUTABLE_PATH) config.executablePath = process.env.PUPPETEER_EXECUTABLE_PATH;
  browser = await puppeteer.launch(config);
  const page = await browser.newPage();
  await page.goto(`http://127.0.0.1:${server.address().port}/`, {waitUntil:'networkidle0'});
  await page.waitForFunction('typeof window.renderDiagram === "function"');
  const rendered = await page.evaluate(source => window.renderDiagram(source), source);
  if (options['--format'] === 'svg') {
    await writeFile(options['--output'], rendered.svg);
  } else {
    await page.setViewport({width:rendered.width, height:rendered.height, deviceScaleFactor:1});
    const element = await page.$('#diagram > svg');
    await element.screenshot({path:options['--output'], type:'png'});
  }
  console.log(JSON.stringify({output:options['--output'], format:options['--format'], width:rendered.width, height:rendered.height}));
} catch (error) {
  console.error(`ERROR: ${error.message}`);
  process.exitCode = 1;
} finally {
  if (browser) await browser.close().catch(() => {});
  if (server) await new Promise(resolve => { server.close(resolve); server.closeAllConnections(); });
}
