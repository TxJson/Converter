import log4js from 'log4js';

// Config files
import config from './config/logconfig.json';

const fn = `${config.DIRECTORY}/${config.FILENAME}.log`;

log4js.configure({
  appenders: {
    output: { type: config.TYPE, filename: fn },
    out: { type: 'stdout' },
  },
  categories: { default: { appenders: ['output', 'out'], level: config.LOGGER_LEVEL } },
});

const logger = log4js.getLogger('output');
logger.level = config.LOGGER_LEVEL;

export {
  logger,
};