import express from 'express';
import { logger } from './logger.mjs';

// Config files
import config from './config/config.json';

// Initialize Server
const app = express.Router();
const rootApp = express();

app.use(express.static(config.CLIENTENTRY));
rootApp.use(config.DEPLOYMENT_ROOT || '/', app);

// Set port
const port = config.PORT || 8080;

// Run app
// http://localhost:PORT/
rootApp.listen(port, () => logger.trace(`Application is running on port ${port}`));