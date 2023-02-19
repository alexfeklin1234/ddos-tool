const Stress = require('ddos-stress');
 
// Create new instance of DDoS Stress
const stress = new Stress();
 
// Run stress on server
stress.run('https://test.com',100);