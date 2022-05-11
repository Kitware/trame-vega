const path = require('path');
const DST_PATH = '../trame_vega/module/serve';

module.exports = {
  outputDir: path.resolve(__dirname, DST_PATH),
  publicPath: './',
  transpileDependencies: ['vega-lite', 'vega'],
};
