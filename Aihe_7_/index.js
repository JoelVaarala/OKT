// Example modified from https://github.com/mqttjs/MQTT.js#example
const mqtt = require('mqtt');

// Vehicle positioning for ongoing buses at Lauttasaari bridge
const myTopic = '/hfp/v2/journey/ongoing/vp/bus/+/+/+/+/+/+/+/+/60;24/18/69/27/#';

// mqtt connects
const hslClient = mqtt.connect('mqtts://mqtt.hsl.fi:8883');
const mosquittoClient = mqtt.connect('mqtt://test.mosquitto.org:1883');

// subscription for location "myTopic"
hslClient.on('connect', function () {
    hslClient.subscribe(myTopic, function (err) {
        if (!err) {
            console.log('Connected!');
        } else {
            console.log(err);
        }
    })
});


hslClient.on('message', function (topic, message) {
    let json = JSON.parse(message.toString());
    let speed = json.VP.spd;
    // console.log(speed);

    // create message with desired info from hslClient
    let myMessage = {
        oper: json.VP.oper,
        veh: json.VP.veh,
        lat: json.VP.lat,
        long: json.VP.long,
        spd: json.VP.spd,
        cause: ""
    }

    if (speed <= 7) {
        // adding desired cause message
        myMessage.cause = "Potential traffic jam"
        // publish message on test.mosquitto
        mosquittoClient.publish('/swd4tn023/30303010/traffic/jam', JSON.stringify(myMessage));
    }
    else if (speed > 9.5) {
        myMessage.cause = "Potential speeding"
        mosquittoClient.publish('/swd4tn023/30303010/traffic/speeding', JSON.stringify(myMessage));
    }

});