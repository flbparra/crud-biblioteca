import './App.css';
import { BrowserRouter as Router,Routes,Route } from 'react-router-dom';
import LoginForm from './components/login/form';

function Login() {
  return (
    <div>
      <LoginForm />
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<Login />} /> 
      </Routes>
    </Router>
  )
}

export default App;
