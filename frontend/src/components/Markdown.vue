<template>
  <div v-html="computedMarkdown"></div>
</template>

<script>
import marked from 'marked'

export default {
  name: 'Markdown',
  props: {
    text: String,
  },
  computed: {
    computedMarkdown() {
      return marked(this.text)
    }
  }
}
</script>