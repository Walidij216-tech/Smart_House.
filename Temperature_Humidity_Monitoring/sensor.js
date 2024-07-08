const sensorLib = require('node-dht-sensor');

const sensor = {
  initialize: function () {
    return sensorLib.initialize(22, 12); // 22 is the sensor type (DHT22), 12 is the GPIO pin number
  },
  read: function () {
    const readout = sensorLib.read();
    console.log(`Temperature: ${readout.temperature.toFixed(2)}°C`);
    console.log(`Humidity: ${readout.humidity.toFixed(2)}%`);
    setTimeout(() => {
      sensor.read();
    }, 2000);
  }
};

if (sensor.initialize()) {
  sensor.read();
} else {
  console.warn('Failed to initialize sensor');
}
