// 문제 출력 영역 요소
const questionBlock = document.getElementById("python-question");

// 서버에서 전달된 정답(hidden input)
const correctAnswer = document.getElementById("correct-answer").value;

// 입력 폼과 결과 메시지 요소
const form = document.getElementById("answer-form");
const input = document.getElementById("user-answer");
const resultMessage = document.getElementById("result-message");

// 폼 제출 이벤트 처리
form.addEventListener("submit", function (e) {
  e.preventDefault(); // 새로고침 방지

  const userInput = input.value.trim();

  if (userInput === correctAnswer) {
    resultMessage.textContent = "🎉 정답입니다! 잘했어요!";
    resultMessage.style.color = "green";
  } else {
    resultMessage.textContent = "❌ 오답입니다. 다시 시도해보세요.";
    resultMessage.style.color = "red";
  }

  input.value = ""; // 입력칸 초기화
});
