var express = require('express');
var router = express.Router();

//models
var Product = require('../models/product');

// Routes
Product.methods(['get', 'put', 'post', 'delete']);
Product.register(router, '/products')

router.get('/products', function(req, res){
	res.send('working')
});

//return router
module.exports = router;
