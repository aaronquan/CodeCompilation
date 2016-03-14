var express = require('express');

var app = express();
var messages = '{ "messages": [' +
				'{"m":"Hello world!", "sentBy": 1, "sentTo": 0},' +
				'{"m":"Hopefully this works", "sentBy": 0, "sentTo": 1},' +
				'{"m":"Goodnight", "sentBy": 0, "sentTo": 1} ]}';

var people = '{ "people": [' +
			'{"firstName":"Mike", "lastName":"Smith"},' +
			'{"firstName":"John", "lastName":"Wong"} ]}'; 

messages = JSON.parse(messages);
people = JSON.parse(people);
app.set('json spaces', 20);


app.get(/messages\/[0-9]*/, function(req, res){
	//res.setHeader('Content-Type', 'application/json');
	var num = req.url.replace(/\/messages\//, '');
	num = parseInt(num);
	res.json(messages.messages[num]);
});
app.get(/people\/[0-9]*/, function(req, res){
	var num = req.url.replace(/\/people\//, '');
	num = parseInt(num);
	res.json(people.people[num]);
});
app.get(/messages/, function(req, res){
	//res.setHeader('Content-Type', 'application/json');
	res.json(messages);
});
app.get(/people/, function(req, res){
	res.json(people);
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