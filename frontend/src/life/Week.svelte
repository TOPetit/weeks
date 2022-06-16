<script>
	let week;
	export let color = "lightgrey";
	export let pos = { x: undefined, y: undefined };
	export let content = "";
	export let selected = { x: undefined, y: undefined };

	function selection() {
		selected = pos;
	}
</script>

{#if content == ""}
	<div
		bind:this={week}
		class="week"
		style="background-color: {color}"
		on:click={selection}
	/>
{:else}
	<div bind:this={week} class="number" style="background-color: {color}">
		<span>{content}</span>
	</div>
{/if}

<style>
	* {
		--size: 12px;
	}

	.week {
		min-width: var(--size);
		max-width: var(--size);
		aspect-ratio: 1;
		cursor: pointer;
	}

	.number {
		min-width: calc(var(--size) * 2);
		aspect-ratio: 2;
		line-height: calc(var(--size) / 2);
		font-size: calc(var(--size) + 3px);
		text-align: center;
	}

	span {
		vertical-align: middle;
		display: inline-block;
		font: bold;
	}
</style>
