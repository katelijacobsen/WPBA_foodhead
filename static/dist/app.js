"use strict";
const FORM_CONTROLS = "input, select, textarea";
// Called by the server through mixhtml
// Top-level functions in a normal script end up on window, which is where mixhtml looks for them.
function markInvalid(fieldId) {
    const element = document.getElementById(fieldId.trim());
    if (!element)
        return;
    // A group (ingredients, instructions) points to its first control
    const control = element.matches(FORM_CONTROLS)
        ? element
        : element.querySelector(FORM_CONTROLS);
    control?.setAttribute("aria-invalid", "true");
    control?.focus();
}
function focusElement(id) {
    const element = document.getElementById(id.trim());
    if (!element)
        return;
    if (!element.hasAttribute("tabindex"))
        element.setAttribute("tabindex", "-1");
    element.focus();
}
function closeDialog(id) {
    document.getElementById(id.trim())?.close();
}
// Screen reader announcements 
function announce(message) {
    const announcer = document.getElementById("announcer");
    if (!announcer)
        return;
    announcer.textContent = "";
    // Clearing first, then setting after a moment, makes the same message announce again
    setTimeout(() => (announcer.textContent = message), 50);
}
// Validation feedback 
// mix-validate only adds the .mix-error class. Mirror it to aria-invalid and focus the first failing field.
new MutationObserver((mutations) => {
    let firstInvalid = null;
    for (const { target } of mutations) {
        const field = target;
        if (!field.hasAttribute("mix-validate"))
            continue;
        const invalid = field.classList.contains("mix-error");
        field.setAttribute("aria-invalid", String(invalid));
        if (invalid && !firstInvalid)
            firstInvalid = field;
    }
    firstInvalid?.focus();
}).observe(document.body, { subtree: true, attributes: true, attributeFilter: ["class"] });
// Clear a field's error as soon as the user starts fixing it
document.addEventListener("input", (event) => {
    const field = event.target;
    if (field.getAttribute("aria-invalid") !== "true")
        return;
    field.removeAttribute("aria-invalid");
    field.classList.remove("mix-error");
    const errorId = field.id
        ? `${field.id}-error`
        : field.closest("fieldset")?.getAttribute("aria-describedby");
    const error = errorId ? document.getElementById(errorId) : null;
    if (error)
        error.textContent = "";
});
// Number stepper
function stepNumber(inputId, direction) {
    const input = document.getElementById(inputId);
    if (!input)
        return;
    // stepUp/stepDown respect the input's own min, max and step
    if (direction === 1)
        input.stepUp();
    else
        input.stepDown();
    input.dispatchEvent(new Event("input", { bubbles: true }));
    const label = input.labels?.[0]?.textContent?.trim() ?? "";
    announce(`${label} ${input.value}`);
}
// Character counter
document.addEventListener("input", (event) => {
    const field = event.target;
    const counterId = field.dataset?.counter;
    if (!counterId)
        return;
    const counter = document.getElementById(counterId);
    if (counter)
        counter.textContent = String(field.value.length);
});
// Ingredient and step rows
// Rows are looked up when a button is clicked, so this also works in forms loaded later by mix-get
function addRow(button) {
    const list = document.getElementById(button.dataset.list ?? "");
    const template = document.getElementById(button.dataset.template ?? "");
    const row = template?.content.firstElementChild?.cloneNode(true);
    if (!list || !row)
        return;
    list.appendChild(row);
    row.querySelector(FORM_CONTROLS)?.focus();
}
function removeRow(button) {
    const row = button.closest("li");
    const list = row?.parentElement;
    if (!row || !list || list.children.length <= 1)
        return; // keep at least one row
    const next = row.nextElementSibling ?? row.previousElementSibling;
    row.remove();
    // Move focus to a neighbouring row so keyboard users don't end up at the top of the page
    next?.querySelector(FORM_CONTROLS)?.focus();
    announce("Removed");
}
function moveRow(button, direction) {
    const row = button.closest("li");
    const list = row?.parentElement;
    const sibling = direction === -1 ? row?.previousElementSibling : row?.nextElementSibling;
    if (!row || !list || !sibling)
        return;
    if (direction === -1)
        sibling.before(row);
    else
        sibling.after(row);
    button.focus();
    const position = Array.from(list.children).indexOf(row) + 1;
    announce(`Moved to step ${position} of ${list.children.length}`);
}
// Drag and drop
document.addEventListener("dragstart", (event) => {
    const row = event.target.closest(".step-entry");
    if (!row)
        return;
    row.classList.add("is-dragging");
    event.dataTransfer?.setData("text/plain", "");
});
document.addEventListener("dragend", () => {
    document.querySelector(".is-dragging")?.classList.remove("is-dragging");
});
document.addEventListener("dragover", (event) => {
    const target = event.target;
    const zone = target.closest(".polaroid");
    if (zone) {
        event.preventDefault();
        zone.classList.add("is-dragover");
        return;
    }
    const dragging = document.querySelector(".is-dragging");
    const over = target.closest(".step-entry:not(.is-dragging)");
    if (!dragging || !over || over.parentElement !== dragging.parentElement)
        return;
    event.preventDefault();
    const { top, height } = over.getBoundingClientRect();
    if (event.clientY < top + height / 2)
        over.before(dragging);
    else
        over.after(dragging);
});
document.addEventListener("dragleave", (event) => {
    event.target.closest(".polaroid")?.classList.remove("is-dragover");
});
document.addEventListener("drop", (event) => {
    const zone = event.target.closest(".polaroid");
    if (!zone || !event.dataTransfer?.files.length)
        return;
    event.preventDefault();
    zone.classList.remove("is-dragover");
    const input = document.getElementById(zone.htmlFor);
    if (!input)
        return;
    input.files = event.dataTransfer.files;
    input.dispatchEvent(new Event("change", { bubbles: true }));
});
// Photo preview 
document.addEventListener("change", (event) => {
    const input = event.target;
    if (!(input instanceof HTMLInputElement) || input.type !== "file")
        return;
    const file = input.files?.[0];
    // File name
    const output = document.getElementById(`${input.id}-name`);
    if (output)
        output.textContent = file ? `Selected: ${file.name}` : "";
    // Show the chosen photo
    const preview = document.getElementById(input.dataset.preview ?? "");
    if (!preview)
        return;
    // Free the previous preview from memory
    const oldUrl = preview.getAttribute("src");
    if (oldUrl?.startsWith("blob:"))
        URL.revokeObjectURL(oldUrl);
    const hasImage = Boolean(file && file.type.startsWith("image/"));
    if (hasImage && file)
        preview.src = URL.createObjectURL(file);
    else
        preview.removeAttribute("src");
    preview.hidden = !hasImage;
    preview.closest(".polaroid")?.classList.toggle("has-photo", hasImage);
});
//# sourceMappingURL=app.js.map