<script>
	import Life from './Life.svelte';
	
	let data = [];
	for (let i = 0; i < 90; i++) {
		data[i] = [];
		for (let j = 0; j < 52; j++) {
			data[i][j] = {color: "lightgrey"}
		}
	}
	
</script>

<Life life={data}/>

