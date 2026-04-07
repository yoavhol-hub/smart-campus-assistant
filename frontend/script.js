const API_URL = "http://127.0.0.1:8000/ask";

const form = document.getElementById("askForm");
const input = document.getElementById("questionInput");
const submitButton = document.getElementById("submitButton");
const clearButton = document.getElementById("clearButton");
const responsePanel = document.getElementById("responsePanel");
const statusArea = document.getElementById("statusArea");
const characterCounter = document.getElementById("characterCounter");
const themeToggle = document.getElementById("themeToggle");
const promptButtons = document.querySelectorAll(".prompt-chip");

function setTheme(mode) {
  document.body.classList.toggle("light", mode === "light");
  localStorage.setItem("smart-campus-theme", mode);
}

(function initTheme() {
  const saved = localStorage.getItem("smart-campus-theme");
  if (saved === "light") {
    setTheme("light");
  }
})();

themeToggle.addEventListener("click", () => {
  const next = document.body.classList.contains("light") ? "dark" : "light";
  setTheme(next);
});

function updateCounter() {
  characterCounter.textContent = `${input.value.length} / 500`;
}

function setLoadingState(isLoading) {
  submitButton.disabled = isLoading;
  submitButton.classList.toggle("is-loading", isLoading);
  statusArea.textContent = isLoading ? "Searching campus data and generating a response..." : "";
}

function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text ?? "";
  return div.innerHTML;
}

function createMetaPill(text, variant = "ok") {
  return `<span class="meta-pill meta-pill--${variant}">${escapeHtml(text)}</span>`;
}

function renderResponse(payload) {
  const category = payload.category || "unknown";
  const usedFallback = Boolean(payload.used_fallback);
  const answer = payload.answer || "No answer returned.";
  const safeQuestion = escapeHtml(payload.question || "");

  responsePanel.classList.remove("empty");
  responsePanel.innerHTML = `
    <article class="answer-card">
      <div>
        <p class="answer-card__headline">Assistant response</p>
        <div class="answer-card__meta">
          ${createMetaPill(`Category: ${category}`)}
          ${usedFallback
            ? createMetaPill("Fallback response used", "fallback")
            : createMetaPill("Retrieved with confidence", "ok")}
        </div>
      </div>

      <div class="answer-card__answer">
        <div class="answer-card__question"><strong>Question:</strong> ${safeQuestion}</div>
        <p>${escapeHtml(answer)}</p>
      </div>

      <div class="answer-card__footer">
        <span class="subtle-note">Live response from your FastAPI backend</span>
        <button class="copy-button" type="button" id="copyAnswerBtn">Copy answer</button>
      </div>
    </article>
  `;

  const copyButton = document.getElementById("copyAnswerBtn");
  copyButton?.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(answer);
      copyButton.textContent = "Copied";
      setTimeout(() => {
        copyButton.textContent = "Copy answer";
      }, 1400);
    } catch {
      copyButton.textContent = "Copy failed";
    }
  });
}

function renderError(message) {
  responsePanel.classList.remove("empty");
  responsePanel.innerHTML = `
    <article class="answer-card">
      <div>
        <p class="answer-card__headline">Something went wrong</p>
        <div class="answer-card__meta">
          ${createMetaPill("Frontend-safe error handling", "fallback")}
        </div>
      </div>
      <div class="answer-card__answer">
        <p>${escapeHtml(message)}</p>
      </div>
    </article>
  `;
}

async function askCampusAssistant(question) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question })
  });

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  return response.json();
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const question = input.value.trim();
  if (!question) {
    statusArea.textContent = "Please enter a question before submitting.";
    input.focus();
    return;
  }

  try {
    setLoadingState(true);
    const payload = await askCampusAssistant(question);
    renderResponse(payload);
  } catch (error) {
    renderError("The frontend could not reach the backend API. Make sure FastAPI is running on http://127.0.0.1:8000.");
  } finally {
    setLoadingState(false);
  }
});

clearButton.addEventListener("click", () => {
  input.value = "";
  updateCounter();
  responsePanel.classList.add("empty");
  responsePanel.innerHTML = `
    <div class="empty-state">
      <div class="empty-state__icon">🎓</div>
      <h3>Your answer will appear here</h3>
      <p>Ask a campus-related question to see the assistant respond with category and answer details.</p>
    </div>
  `;
  statusArea.textContent = "";
  input.focus();
});

promptButtons.forEach((button) => {
  button.addEventListener("click", () => {
    input.value = button.dataset.prompt || "";
    updateCounter();
    input.focus();
  });
});

input.addEventListener("input", updateCounter);
input.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    form.requestSubmit();
  }
});

updateCounter();
