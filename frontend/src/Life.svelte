<script>
	import Year from "./Year.svelte";
	export let life = [];
	let previous_selection = undefined;
	let selected = undefined;

	function changeColor(new_element) {
		if (new_element) {
			if (previous_selection) {
				previous_selection.style.backgroundColor = "lightgrey";
			}
			if (new_element != previous_selection) {
				previous_selection = new_element;
				previous_selection.style.backgroundColor = "red";
			}
		}
	}

	$: selected, changeColor(selected);
</script>

<div class="life">
	{#each life as year, i}
		<Year {year} year_id={i} bind:selected />
	{/each}
</div>

<style>
	.life {
		margin: auto;
		width: 700px;
		display: flex;
		flex-direction: column;
		justify-content: center;
		gap: 2px;
	}
</style>
