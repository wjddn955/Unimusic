$(document).ready(function () {
    const $audioEl = document.querySelector("audio");
    const $btn1 = document.querySelector("#recording-btn");
    let isRecording = false;
    let mediaRecorder = null;
    const audioArray = [];

    $btn1.onclick = async function (event) {
        if (!isRecording) {

            const mediaStream = await navigator.mediaDevices.getUserMedia({audio: true});
            mediaRecorder = new MediaRecorder(mediaStream);
            mediaRecorder.ondataavailable = (event) => {
                audioArray.push(event.data);
            }
            mediaRecorder.onstop = (event) => {

                const blob = new Blob(audioArray, {"type": "audio/ogg codecs=opus"});
                audioArray.splice(0); // 기존 오디오 데이터들은 모두 비워 초기화한다.
                const blobURL = window.URL.createObjectURL(blob);
                $audioEl.src = blobURL;
                $audioEl.play();
                $('#submit-btn').click(function (){
                    sendBlobToBackend(blob);
                })
            }
            mediaRecorder.start();
            isRecording = true;

        } else {
            mediaRecorder.stop();
            isRecording = false;
        }
    }
})

function sendBlobToBackend(blob) {
    const formData = new FormData();
    formData.append('audio_file', blob, 'recording.mp3');

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/input/'); // 백엔드의 API 엔드포인트 URL로 수정해야 합니다.
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.onload = function () {
        if (xhr.status === 201) {
            console.log('음성 파일이 성공적으로 전송되었습니다.');
        } else {
            console.error('음성 파일 전송에 실패했습니다. 상태 코드: ', xhr.status);
        }
    };
    xhr.send(formData);
}
