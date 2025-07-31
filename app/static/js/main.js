document.addEventListener("DOMContentLoaded", function () {
	const expenseCategories = [
		{ id: "utilities", icon: "💡", label: "Utilities" },
		{ id: "entertainment", icon: "🎭", label: "Entertainment" },
		{ id: "school_fees", icon: "📚", label: "School Fees" },
		{ id: "shopping", icon: "🛍️", label: "Shopping" },
		{ id: "healthcare", icon: "🏥", label: "Healthcare" },
	];
	const expensesContainer = document.getElementById("expenses");

	expenseCategories.forEach((category) => {
		const item = document.createElement("div");
		item.className = "row g-3 align-items-center mb-3 p-2";

		item.innerHTML = `
            <div class="col-auto">
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="expense_${category.id}" name="expense_${category.id}">
                    <label class="form-check-label" for="expense_${category.id}">
                        ${category.icon} ${category.label}
                    </label>
                </div>
            </div>
            <div class="col">
                <div class="input-group">
                    <span class="input-group-text">$</span>
                    <input type="number" class="form-control" name="amount_${category.id}" 
                           placeholder="0.00" step="0.01" min="0" max="999999999.99" disabled
                           oninput="this.value = this.value.replace(/[^0-9.]/g, ''); if(parseFloat(this.value) > 999999999.99) this.value = 999999999.99;"
                           aria-label="${category.label} amount">
                </div>
            </div>
        `;

		expensesContainer.appendChild(item);

		const checkbox = item.querySelector('input[type="checkbox"]');
		const amountInput = item.querySelector('input[type="number"]');

		checkbox.addEventListener("change", function () {
			amountInput.disabled = !this.checked;
			if (!this.checked) {
				amountInput.value = "";
			} else {
				amountInput.focus();
			}
		});
	});
});
