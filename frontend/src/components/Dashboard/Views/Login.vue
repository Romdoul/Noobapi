<template>
	<div class="row">
		<div class="col-md-12">
		<div class="card">
			<paper-table :title="table1.title" :sub-title="table1.subTitle" :data="table1.data" :columns="table1.columns">

			</paper-table>
		</div>
		</div>

	</div>
</template>
<script>
	import PaperTable from 'components/UIComponents/PaperTable.vue'
	const tableColumns = ['Id', 'Name', 'Salary', 'Country', 'City', 'Actions']
	const tableData = []

	export default {
		components: {
			PaperTable
		},
		data () {
			return {
			table1: {
				title: 'Stripped Table',
				subTitle: 'Here is a subtitle for this table',
				columns: [...tableColumns],
				data: [...tableData]
			},
			table2: {
				title: 'Table on Plain Background',
				subTitle: 'Here is a subtitle for this table',
				columns: [...tableColumns],
				data: [...tableData]
			}
			}
		},
		mounted: ()=>{
			this.tableData = [{
					id: 1,
					name: 'Tadashi Hamada',
					salary: '$36.738',
					country: 'Niger',
					city: 'Oud-Turnhout',
					actions: 'View, Evaluate, Delete'
				},
				{
					id: 2,
					name: ' Romdoul ',
					salary: '$23,789',
					country: 'Curaçao',
					city: 'Sinaai-Waas',
					actions: 'View, Evaluate, Delete'
				},
				{
					id: 3,
					name: 'Sage Rodriguez',
					salary: '$56,142',
					country: 'Netherlands',
					city: 'Baileux',
					actions: 'View, Evaluate, Delete'
				},
				{
					id: 4,
					name: 'Philip Chaney',
					salary: '$38,735',
					country: 'Korea, South',
					city: 'Overland Park',
					actions: 'View, Evaluate, Delete'
				},
				{
					id: 5,
					name: 'Doris Greene',
					salary: '$63,542',
					country: 'Malawi',
					city: 'Feldkirchen in Kärnten',
					actions: 'View, Evaluate, Delete'
				}
			]
		}
	}

</script>
<style>

</style>
