import React from "react";

export default function LoginForm(){
  return (
    <div>
      <form action="#">
        <div>
          <label htmlFor="user">
            Usuário:          
          </label>
          <input type="text" id="user" name="user" autoComplete="user" placeholder="Usuário" />
        </div>
        <div>
          <label htmlFor="password">
            Senha:          
          </label>
          <input type="password" id="password" name="password" autoComplete="password" placeholder="Senha" />
        </div>
      </form>
    </div>
  )
}