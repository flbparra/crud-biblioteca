import React, { useState}from "react";

export default function SignUpForm(){
  const [funcao,setFuncao] = useState("");
  
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
  
  return(
    <div>
      <form>
        <div>
          <label htmlFor="login">
            Login:
          </label>
          <input type="text" id="login" name="login" autoComplete="login" placeholder="Login" />
        </div>
        <div>
          <label htmlFor="senha">
            Senha:
          </label>
          <input type="password" id="senha" name="senha" autoComplete="senha" placeholder="Senha" />
        </div>
        <div>
        <label htmlFor="nome">
          Nome:
        </label>
        <input type="text" id="nome" name="nome" autoComplete="nome" placeholder="Nome" />
        </div>
        <div>
        <label htmlFor="sobrenome">
          Sobrenome:
        </label>
        <input type="text" id="sobrenome" name="sobrenome" autoComplete="sobrenome" placeholder="Sobrenome" />
        </div>
        <div onChange={(e)=>setFuncao(e.target.value)}> 
          <label htmlFor="funcao">
            Função:
          </label>
          <input type="radio" id="admin" name="funcao" value="admin" />
          <label for="admin">
            Admin</label>
          <input type="radio" id="usuario" name="funcao" value="usuario" />
          <label for="usuario">
            Usuário</label>
        </div>
        <button onClick={()=>{alert(funcao)}}>
          Cadastrar
        </button>
      </form>
    </div>

  )


}
