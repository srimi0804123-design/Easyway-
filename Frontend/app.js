const BASE_URL = "http://localhost:8000"; // FastAPI default

const output = document.getElementById("output");

// ---------- Health Check ----------
document.getElementById("healthBtn").onclick = async () => {
  const res = await fetch(`${BASE_URL}/`);
  const data = await res.json();
  document.getElementById("healthStatus").innerText = data.status;
};

// ---------- Text-based Expense ----------
document.getElementById("parseTextBtn").onclick = async () => {
  const text = document.getElementById("expenseText").value;

  if (!text) {
    alert("Please enter expense text");
    return;
  }

  const formData = new FormData();
  formData.append("text", text);
  formData.append("source", "manual");

  const res = await fetch(`${BASE_URL}/parse-expense`, {
    method: "POST",
    body: formData,
  });

  const data = await res.json();
  output.textContent = JSON.stringify(data, null, 2);
};

// ---------- Image-based Expense ----------
document.getElementById("parseImageBtn").onclick = async () => {
  const fileInput = document.getElementById("imageInput");

  if (!fileInput.files.length) {
    alert("Please select an image");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  const res = await fetch(`${BASE_URL}/parse-expense-image`, {
    method: "POST",
    body: formData,
  });

  const data = await res.json();
  output.textContent = JSON.stringify(data, null, 2);
};
// ---------- Section Navigation ----------
function showSection(id) {
  document.querySelectorAll(".section").forEach(sec => {
    sec.classList.remove("active");
  });
  document.getElementById(id).classList.add("active");
}
// ---------------- CATEGORY LOGIC ----------------
let selectedCategories = [];

// Toggle select/unselect
document.addEventListener("click", (e) => {
  if (e.target.classList.contains("category-item")) {
    const value = e.target.innerText;

    e.target.classList.toggle("selected");

    if (selectedCategories.includes(value)) {
      selectedCategories = selectedCategories.filter(v => v !== value);
    } else {
      selectedCategories.push(value);
    }

    console.log("Selected Categories:", selectedCategories);
  }
});

// Add new category
function addCategory() {
  const input = document.getElementById("newCategoryInput");
  const value = input.value.trim();

  if (!value) return;

  const div = document.createElement("div");
  div.className = "category-item";
  div.innerText = value;

  document.getElementById("categoryList").appendChild(div);
  input.value = "";
}

/* --------- Existing backend code stays below --------- */
// health check
// parse expense
// parse image