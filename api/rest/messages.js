var express = require('express');

var app = express();
var messages = '{ "messages": [' +
				'"Hello world!",' +
				'"Hopefully this works",' +
				'"Goodnight" ]}';

messages = JSON.parse(messages);

app.get(/messages\/[0-9]*/, function(req, res){
	var num = req.url.replace(/\/messages\//, '');
	num = parseInt(num);
	res.send(messages.messages[num]);
});
app.get(/messages/, function(req, res){
	res.send(messages);
});
app.get(/[a-z]*/, function(req, res){
	res.send("An API request for messages: request /messages. "+
			 "If you want a specific message: request /messages/[0-9]*");
});
app.get('', function(req, res){
	res.send("An API request for messages: request /messages. "+
			 "If you want a specific message: request /messages/[0-9]*");
});

app.listen(3000);