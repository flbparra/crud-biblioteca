import React, { useState} from "react";

export default function LoginForm(){
  const [user,setUser] = useState("");
  const [password,setPassword] = useState("");
  
  
  const buttonClick = async () => {
    const response = await fetch(`http://127.0.0.1:5000/login`,{
      method: "POST",
      body: JSON.stringify({
        "Login": user,
        "Senha": password
      }),
      mode: "cors",
      headers: {
        "Content-Type": "application/json"
      }
    }).then((response)=>{
      if(response.status === 404){
        alert("Usuário não encontrado")
      }
      else if(response.status===401){
        alert("Senha incorreta")
      }
      else{
        sessionStorage.setItem("userData",response.body)
      }
    })
  }
  
  return (
    <div>
      <form action="#">
        <div>
          <label htmlFor="user">
            Usuário:          
          </label>
          <input type="text" id="user" name="user" autoComplete="user" placeholder="Usuário" value={user} onChange={(e)=>setUser(e.target.value)} />
        </div>
        <div>
          <label htmlFor="password">
            Senha:          
          </label>
          <input type="password" id="password" name="password" autoComplete="password" placeholder="Senha" value={password} onChange={(e)=>setPassword(e.target.value)} />
        </div>
        <div>
          <button onClick={buttonClick}>
            Login
          </button>
        </div>
      </form>
    </div>
  )
}