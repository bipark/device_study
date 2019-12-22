var express = require('express');
var router = express.Router();
const Gpio = require('pigpio').Gpio;

const L298N = require('./l298n.js');
let l298n = new L298N(17,27,22,14,15,18);

l298n.setSpeed(l298n.NO1,5);
l298n.setSpeed(l298n.NO2,5);

/* GET home page. */
router.get('/start', function(req, res, next) {
  l298n.forward(l298n.NO1);
  l298n.forward(l298n.NO2);
  res.render('index', { title: 'Start' });
});

router.get('/stop', function(req, res, next) {
  l298n.stop(l298n.NO1);
  l298n.stop(l298n.NO2);
  res.render('index', { title: 'Stop' });
});

module.exports = router;
