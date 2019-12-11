var aes256=require('aes256')
var mqtt = require('mqtt')
var client = mqtt.connect('mqtt://192.168.75.140')
var key="art"
client.on('connect', function () {

client.subscribe('topic')
//client.subscribe('client/dead')
})


client.on('message', function (topic, message) {
  // message is Buffer

  console.log(message.toString())

//  client.end()
})

