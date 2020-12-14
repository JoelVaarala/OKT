const Redux = require('redux')

//Action 1
function addColor(value){
    return{
        type: "ADD", //add
        color: value //value param
    };
}

//Action 2
function removeColor(value){
    return{
        type: "REMOVE", //remove
        color: value //value param
    };
}


function favoriteColors(state, action){ 
    if(state == undefined){
        state = []
    }

    if(action.type === "ADD"){
        return state.concat(action.color);
    }else if(action.type === "REMOVE"){
        return state.filter(function(item){ 
            return item !== action-color;
        });
    }else{
        return state;
    }
}

let store = Redux.createStore(favoriteColors);
store.dispatch(addColor("sininen"));
store.dispatch(addColor("keltainen"));
store.dispatch(addColor("vihreä"));
store.dispatch(removeColor("sininen"));

console.log(store.getState()); // palauttaa : ['keltainen', 'vihreä']

