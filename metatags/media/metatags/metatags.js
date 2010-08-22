(function($){
	$(document).ready(function(){
		// Add anchor tag for Show/Hide link
		$("#metatags-metatag-content_type-object_id-group").each(function(i, elem) {
			// Don't hide if fields in this fieldset have errors
			if ( $(elem).find("div.errors").length == 0 ) {
				$(elem).addClass("collapsed");
				$(elem).find("h2").first().append(' (<a id="fieldsetcollapser' +
					i +'" class="collapse-toggle" href="#">' + gettext("Show") +
					'</a>)');
			}
		});
		// Add toggle to anchor tag
		$("#metatags-metatag-content_type-object_id-group a.collapse-toggle").toggle(
			function() { // Show
				$(this).text(gettext("Hide"));
				$(this).closest(".inline-group").removeClass("collapsed");
				return false;
			},
			function() { // Hide
				$(this).text(gettext("Show"));
				$(this).closest(".inline-group").addClass("collapsed");
				return false;
			}
		);
	});
})(django.jQuery);