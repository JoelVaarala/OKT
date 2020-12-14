const fetch = require('node-fetch');


async function getUserPosts(){
    let resultsArray = []
    const users = await fetch('https://jsonplaceholder.typicode.com/users')
    const posts = await fetch('https://jsonplaceholder.typicode.com/posts')
    const us = await users.json()
    const ps = await posts.json()
    us.forEach(user => {
        let posted = ps.filter(pos => pos.userId == user.id)
        resultsArray.push({
            user: user,
            posts: posted
        })
    })
    console.log('Results : ' , resultsArray)
    return(resultsArray)
}

module.exports = { getUserPosts };


/*async function getUserPost() {
    let tiedot = [];
    Promise.all([
     fetch('https://jsonplaceholder.typicode.com/users'),
     fetch('https://jsonplaceholder.typicode.com/posts'),
    ])
    .then(async([fetch1, fetch2]) => {
        // return Promise.all(response.map((res) => {
        //     return res.json();
        // }));
        const a = await fetch1.json();
        const b = await fetch2.json();
        return [a,b]
    })
    .then(async(data) => {
        let resultArray = [];
        data[0].forEach(element => {
            let posted = data[1].filter(pos => pos.userId == element.id)
            
            resultArray.push({
                userWithPosts:  element,
                posts: posted
            });
        });

        tiedot = await resultArray;
        //console.log('posted dataa : ', tiedot[1])
        return resultArray;
        //console.log('0 taulu : ',data[0]) // sis userit
        //console.log('1 taulu : ',data[1]) // sis postaukset
    })
    .catch((err) => {
        console.log(err, ' error - error')
    })
    // ei return onnistunut, muutamista yrityksistä huolimatta
} */