import logo from './logo.svg';
import './App.css';

import Home from './pages/Home'
import Tableau from './pages/table2'

import BarGraph from './pages/ess'
import Sample from './pages/sample'
import { Routes, Route, BrowserRouter } from "react-router-dom"



function App() {
  return (<>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />}></Route>
        <Route path='/table' element={<Tableau />}></Route>
        <Route path='/sample' element={<Sample />}></Route>
        <Route path='/harsh' element={<BarGraph />}></Route>
      </Routes>
    </BrowserRouter>
    
    </>

  );
}

export default App;
