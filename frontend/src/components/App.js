import React from 'react'
import ReactDOM from 'react-dom'	
import {BrowserRouter, Route,Routes} from 'react-router-dom'
import HomePage from './HomePage.js'
import CreateRoomPage from './CreateRoomPage.js'
import JoinRoomPage from './JoinRoomPage.js'

export default function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<HomePage/>}/>
          <Route path="/create" element={<CreateRoomPage/>}/>
          <Route path="/join" element={<JoinRoomPage/>}/>
        </Routes>
      </BrowserRouter>
    </>
  )
}

ReactDOM.render(<App/>, document.getElementById('app'))