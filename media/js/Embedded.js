// inject iframe and fire event	
var loadResult = function () {
	new Element('iframe', {
		'src': show_src,
		'styles': {
			'height': height - 10
		}
	}).inject($('result'));
	this.removeEvent('click',loadResult);
	window.fireEvent('result_included');
};


Element.implement({
	switchLighter: function(lighter_class) {		
		var resizeLighter = function( light ) {
			// recursive function
			if (light.element) {
				resize_element_counter = 0;
				return light.element.setStyle('height', height);
			}
			if (resize_element_counter++ < 200 ) (function(){
				return resizeLighter(light);
			}).delay(1);
		};
		lighter_class = lighter_class || 'standard';
		// destroy all previous lighters, and create a new one 
		// from the currently selected (but only if it's not the Result tab)
		$$('.'+lighter_class+'Lighter').destroy();
		if (this.get('tag') == 'pre') {
			var light = this.light({flame: lighter_class});
			resizeLighter(light);
			return light;
		}
	}
});

this.switchTab = function(action, index) {
	this.sections.removeClass('active');
	this.sections[index].addClass('active');
	this.actions.getParent().removeClass('active');
	action.getParent().addClass('active');
	this.sections[index].switchLighter();
}


