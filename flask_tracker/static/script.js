document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("itemForm");
    const container = document.getElementById("itemsContainer");
    const searchInput = document.getElementById("searchInput");
    const statusFilter = document.getElementById("statusFilter");

    // Load items from API
    async function loadItems() {
        const res = await fetch("/api/items");
        const data = await res.json();
        displayItems(data.items);
    }

    function displayItems(items) {
        container.innerHTML = "";
        const searchTerm = searchInput.value.toLowerCase();
        const statusTerm = statusFilter.value;

        items.filter(item => {
            const matchesSearch = item.title.toLowerCase().includes(searchTerm);
            const matchesStatus = statusTerm === "all" || item.status === statusTerm;
            return matchesSearch && matchesStatus;
        }).forEach(item => {
            const card = document.createElement("div");
            card.className = "card";
            card.innerHTML = `
                <h3>${item.title}</h3>
                <p><strong>Genre:</strong> ${item.genre || "N/A"}</p>
                <p><strong>Rating:</strong> ${item.rating || "N/A"}</p>
                <p><strong>Notes:</strong> ${item.notes || ""}</p>
                <p><strong>Status:</strong> ${item.status}</p>
                <button onclick="toggleStatus(${item.id})">${item.status === "completed" ? "Mark Want" : "Mark Completed"}</button>
                <button onclick="confirmDelete(${item.id})">Delete</button>
            `;
            container.appendChild(card);
        });
    }

    // Add item via AJAX
    form.addEventListener("submit", async e => {
        e.preventDefault();
        const itemData = {
            title: document.getElementById("title").value,
            genre: document.getElementById("genre").value,
            rating: document.getElementById("rating").value,
            notes: document.getElementById("notes").value
        };
        const res = await fetch("/add", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(itemData)
        });
        const result = await res.json();
        if (result.success) {
            form.reset();
            loadItems();
        } else {
            alert(result.error);
        }
    });

    // Delete item with confirmation
    window.confirmDelete = async id => {
        if (confirm("Are you sure you want to delete this item?")) {
            await fetch(`/api/delete/${id}`, {method: "DELETE"});
            loadItems();
        }
    };

    // Toggle status
    window.toggleStatus = async id => {
        await fetch(`/api/toggle/${id}`, {method: "POST"});
        loadItems();
    };

    // Search/filter
    searchInput.addEventListener("input", loadItems);
    statusFilter.addEventListener("change", loadItems);

    // Initial load
    loadItems();
});
