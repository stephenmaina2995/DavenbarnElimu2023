import React from 'react'
import {View,Text} from 'react-native';

function Home(props) {
  return (
    <View>
      <Text>Open up App.js to start working on your app!</Text>
      <Text>{props.name}</Text>
    </View>
  )
}

export default Home
