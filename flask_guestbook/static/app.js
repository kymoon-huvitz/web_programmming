const el = {
  form: document.getElementById("form"),
  name: document.getElementById("name"),
  message: document.getElementById("message"),
  submitBtn: document.getElementById("submitBtn"),
  status: document.getElementById("status"),
  list: document.getElementById("list"),
  refreshBtn: document.getElementById("refreshBtn"),
};

function setStatus(text) {
  el.status.textContent = text || "";
}

function row(item) {
  // XSS 방지: textContent로 삽입
  const div = document.createElement("div");
  div.className = "item";
  const name = document.createElement("div");
  const msg = document.createElement("div");
  name.className = "name";
  msg.className = "message";
  name.textContent = item.name || "익명";
  msg.textContent = item.message || "";
  div.appendChild(name);
  div.appendChild(msg);
  return div;
}

async function loadMessages() {
  el.list.textContent = "불러오는 중...";
  try {
    const res = await fetch("/messages");
    if (!res.ok) throw new Error("목록을 가져오지 못했습니다.");
    const data = await res.json();
    el.list.textContent = "";
    if (!Array.isArray(data) || data.length === 0) {
      el.list.textContent = "아직 메시지가 없습니다. 첫 번째 글을 남겨보세요!";
      return;
    }
    // 최근 글이 아래로 쌓였으면 위로 보이게 역순 표시 (원하면 지우세요)
    [...data].reverse().forEach((item) => el.list.appendChild(row(item)));
  } catch (err) {
    el.list.textContent = `에러: ${err.message}`;
  }
}

async function submitMessage(e) {
  e.preventDefault();
  setStatus("");
  const name = (el.name.value || "익명").trim();
  const message = (el.message.value || "").trim();
  if (!message) {
    setStatus("메시지는 필수입니다.");
    el.message.focus();
    return;
  }

  el.submitBtn.disabled = true;
  el.submitBtn.textContent = "전송 중...";

  try {
    const res = await fetch("/messages", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, message }),
    });
    if (!res.ok) {
      const errJson = await res.json().catch(() => ({}));
      throw new Error(errJson.error || "전송 실패");
    }
    setStatus("등록 완료!");
    el.message.value = "";
    await loadMessages();
  } catch (err) {
    setStatus(`에러: ${err.message}`);
  } finally {
    el.submitBtn.disabled = false;
    el.submitBtn.textContent = "등록";
  }
}

el.form.addEventListener("submit", submitMessage);
el.refreshBtn.addEventListener("click", loadMessages);

// 초기 로드
loadMessages();
