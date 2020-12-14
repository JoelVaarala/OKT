const express = require('express');
const app = express();
const port = 3000;

// const { getUsers } = require('./requests/UsersReq');
// const { getPosts } = require('./requests/PostsReq');
const { getUserPosts } = require('./requests/RequestData');


app.get('/users', async function(req, res){

     getUserPosts().then(data => {
         res.json(data)
         //console.log('index.js: ', data)
     })

})

app.listen(port,() => console.log('running at : ', port) );