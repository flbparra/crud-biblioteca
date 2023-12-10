import React, { useState}from "react";

export default function SignUpForm(){
  const [funcao,setFuncao] = useState("");
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
          <input type="password" id="senha" name="senha" autoComplete="senha" placeholder="Senha" /><br />
        </div>
        <label htmlFor="nome">
          Nome:
        </label>
        <input type="text" id="nome" name="nome" autoComplete="nome" placeholder="Nome" /><br />
        <label htmlFor="sobrenome">
          Sobrenome:
        </label>
        <input type="text" id="sobrenome" name="sobrenome" autoComplete="sobrenome" placeholder="Sobrenome" /><br />
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
