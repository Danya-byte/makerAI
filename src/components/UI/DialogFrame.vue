<template>
    <main class="dialog-frame">
        <div class="chat">
            <div class="preview">
                <div style="display: flex; align-items: center; justify-content: center;">
                    <img width="130px" height="130px" src="@/assets/logo.png" alt="logo">
                </div>
                <div>
                    <h1 class="logo-text">Maker_AI</h1>
                </div>
            </div>
            <nav class="input">
                <div class="type">
                    <div style="width: 100%;">
                        <input type="text" placeholder="Ask to MakerAI">
                    </div>
                    <div class="send">
                        <svg xmlns="http://www.w3.org/2000/svg" width="25" height="24" viewBox="0 0 25 24" fill="none">
                            <g>
                                <path d="M11.5 20V7.825L5.9 13.425L4.5 12L12.5 4L20.5 12L19.1 13.425L13.5 7.825V20H11.5Z" fill="#aaaaaa"/>
                            </g>
                        </svg>
                    </div>
                </div>
            </nav>
        </div>
    </main>
</template>

<style scoped>
.dialog-frame {
	background: #1b1b1b;
    border-radius: 5px;
    border: 10px solid #111111;
    border-radius: 20px;
    display: grid;
    align-items: self-end;
    justify-content: right;
}

.preview {
	display: grid;
	align-items: center;
}

.logo-text {
	font-size: 31px;
	color: #f0f0f0;
	font-family: monospace;
	font-weight: 400;
}


.chat {
	width: calc(100vw - 240px);
    height: calc(100vh - 20px);
    position: relative;
    display: grid;
    align-items: center;
    justify-content: center;
}

.input {
	padding: 5px;
	display: grid;
    align-items: center;
    position: absolute;
    bottom: 0;
    justify-content: center;
    width: -webkit-fill-available;
}

.type {
	border: 0.5px solid #aaaaaa;
    border-radius: 5px;
    margin: 10px;
    width: 50vw;
    padding: 10px;
    display: flex;
    gap: 10px;
    justify-content: space-between;
    align-items: center;
}

input {
	background: transparent;
	border: 0;
	color: #f0f0f0;
	font-size: 18px;
	font-family: 'Inter';
	width: 100%;
}

input:focus {
	outline: none;
}

.send {
	display: flex;
    align-items: center;
    padding: 5px;
    background: #492410;
    width: fit-content;
    border-radius: 5px;
}

</style>