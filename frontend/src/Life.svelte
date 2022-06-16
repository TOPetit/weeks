<script>
	import { spread } from "svelte/internal";

	import Year from "./Year.svelte";
	export let life = [];
	let prev_selected = { x: undefined, y: undefined };
	let selected = { x: undefined, y: undefined };

	function changeColor() {
		if (prev_selected.x + prev_selected.y >= 0) {
			// A week was selected
			if (selected.x + selected.y >= 0) {
				// A week is selected
				if (
					selected.x == prev_selected.x &&
					selected.y == prev_selected.y
				) {
					// The week previously selected if the same as the new one
					// We remove the coloration on this week, and reset prev_selected
					life[selected.x][selected.y].color = "lightgrey";
					prev_selected = { x: undefined, y: undefined };
				} else {
					// There is a new week selected, and a different previous week
					life[prev_selected.x][prev_selected.y].color = "lightgrey";
					life[selected.x][selected.y].color = "red";
					prev_selected = selected;
				}
			}
		} else {
			if (selected.x + selected.y >= 0) {
				life[selected.x][selected.y].color = "red";
				prev_selected = selected;
			}
		}
	}

	$: selected, changeColor();
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
		gap: 4px;
	}
</style>
