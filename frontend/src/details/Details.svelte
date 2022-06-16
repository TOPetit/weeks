<script>
    export let pos;
    let display = { x: "", y: "" };

    let details;

    function updateDisplay() {
        if (details) {
            details.style.visibility =
                pos.x + pos.y >= 0 ? "visible" : "hidden";
        }

        display.x = pos.x >= 0 ? String(pos.x) : "";
        display.y = pos.y >= 0 ? String(pos.y) : "";
    }

    $: pos, updateDisplay();
</script>

<div bind:this={details} class="details">
    <h1>{display.x}<br />{display.y}</h1>
</div>

<style>
    .details {
        width: 500px;
        height: 500px;
        border: 1px solid red;
    }
</style>
