<script>
	import Week from "./Week.svelte";
	export let year = [];
	export let year_id = 0;
	export let selected = { x: undefined, y: undefined };
</script>

<div class="year">
	{#if year_id % 5 == 0}
		<Week
			color={"rgba(0, 0, 0, 0)"}
			content={String(year_id).padStart(2, "0")}
			bind:selected
		/>
	{:else}
		<Week color={"rgba(0, 0, 0, 0)"} content={" "} bind:selected />
	{/if}
	{#each year as { color, pos }, i}
		<Week {color} {pos} bind:selected />
	{/each}
</div>

<style>
	.year {
		margin: auto;
		width: 100%;
		display: flex;
		justify-content: center;
		gap: 4px;
	}
</style>
