async function scrape() {
    const keyword = document.getElementById("keyword").value;
    const results = document.getElementById("results");
    results.innerHTML = "<li>Loading...</li>";

    try {
        const res = await fetch("http://127.0.0.1:5000/scrape", {

            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ keyword }),
        });

        const data = await res.json();
        results.innerHTML = "";

        if (data.articles && data.articles.length > 0) {
            data.articles.forEach((article) => {
                const li = document.createElement("li");
                li.innerHTML = `
                    <a href="${article.link}" target="_blank">${article.title}</a>
                    <div class="timestamp">${article.time}</div>
                    <div class="summary">${article.summary}</div>
                `;
                results.appendChild(li);
                console.log("Keyword sent:", keyword);
                console.log("Response from server:", data);

            });
        } else {
            results.innerHTML = "<li>No articles found for that keyword.</li>";
        }
    } catch (err) {
        console.error("Scrape error:", err);
        results.innerHTML = "<li>Something went wrong. Check console.</li>";
    }
}
