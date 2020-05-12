import React from 'react';
import Request from 'superagent';
import { FormGroup, InputGroup, Divider } from "@blueprintjs/core";
import './LoginPage.css';
import { navigate } from "@reach/router"

function Login() {

    const [createEmail, setCreateEmail] = React.useState("");
    const [createEmailHelper, setCreateEmailHelper] = React.useState("");
    const [createPassword, setCreatePassword] = React.useState("");
    const [createPasswordHelper, setCreatePasswordHelper] = React.useState("");

    const [loginEmail, setLoginEmail] = React.useState("");
    const [loginEmailHelper, setLoginEmailHelper] = React.useState("");
    const [loginPassword, setLoginPassword] = React.useState("");
    const [loginPasswordHelper, setLoginPasswordHelper] = React.useState("");

    function createEmailOnChange(event) {
        setCreateEmail(event.target.value);
        setCreateEmailHelper("");
    }

    function createPasswordOnChange(event) {
        setCreatePassword(event.target.value);
        setCreatePasswordHelper("");
    }

    function loginEmailOnChange(event) {
        setLoginEmail(event.target.value);
        setLoginEmailHelper("");
    }

    function loginPasswordOnChange(event) {
        setLoginPassword(event.target.value);
        setLoginPasswordHelper("");
    }

    function isEmailValid(email) {
        return email.match(/^([\w.%+-]+)@([\w-]+\.)+([\w]{2,})$/i);
    }

    function handleCreateAccount() {
        if (!isEmailValid(createEmail)) {
            setCreateEmailHelper("Email is invalid");
            return;
        } else if (createPassword.length < 5) {
            setCreatePasswordHelper("password should be at least 5 characters long");
            return;
        }

        const requestObject = {
            name: createEmail
        }
        const url = "http://127.0.0.1:8000/chorescheduling";
        Request.post(url).send(requestObject);
        console.log("email and password are valid");
        navigate('home');
    }

    function handleLogin() {
        if (!isEmailValid(loginEmail)) {
            setLoginEmailHelper("email is invalid");
            return;
        }

        // TODO: verify email and password with database
        navigate('home');
    }

    return (
        <div id="login">
            <div>
                <h2>Create an account</h2>

                <FormGroup inline={true} label="Email" labelFor="text-input" helperText={createEmailHelper}>
                    <InputGroup id="email" placeholder="E-mail address" value={createEmail} onChange={createEmailOnChange} />
                </FormGroup>

                <FormGroup label="Password" labelFor="text-input" inline={true} helperText={createPasswordHelper}>
                    <InputGroup id="password" placeholder="Password" value={createPassword} onChange={createPasswordOnChange}/>
                </FormGroup>

                <button disabled={!createEmail || !createPassword} onClick={handleCreateAccount}>Create an account</button>
            </div>
            <Divider id="divider"/>
            <div>
                <h2>Log in</h2>

                <FormGroup label="Email" labelFor="text-input" inline={true} helperText={loginEmailHelper}>
                    <InputGroup id="login-email" placeholder="E-mail address" value={loginEmail} onChange={loginEmailOnChange}/>
                </FormGroup>

                <FormGroup label="Password" labelFor="text-input" inline={true} helperText={loginPasswordHelper}>
                    <InputGroup id="login-password" placeholder="Password" value={loginPassword} onChange={loginPasswordOnChange}/>
                </FormGroup>

                <button disabled={!loginEmail || !loginPassword} onClick={handleLogin}>Login</button>
            </div>
        </div>
    )
}

export default Login;