import './App.css';
import { BrowserRouter as Router,Routes,Route } from 'react-router-dom';
import LoginForm from './components/login/form';
import SignUpForm from './components/login/SignUp';

function Login() {
  return (
    <div>
      <LoginForm />
      <hr />
      <SignUpForm />
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
