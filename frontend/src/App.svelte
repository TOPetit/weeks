<script>
	import Life from "./life/Life.svelte";
	import Details from "./details/Details.svelte";

	let selected = { x: undefined, y: undefined };

	let data = [];
	for (let i = 0; i < 90; i++) {
		data[i] = [];
		for (let j = 0; j < 52; j++) {
			data[i][j] = { color: "lightgrey", pos: { x: i, y: j } };
		}
	}
</script>

<div class="container-app">
	<Life life={data} bind:prev_selected={selected} />
	<Details pos={selected} />
</div>

<style>
	.container-app {
		width: 90%;
		margin: auto;
		display: flex;
		justify-content: center;
		gap: 50px;
	}
</style>
