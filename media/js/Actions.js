/*
 * Define actions on the run/save/clean buttons
 */
var MooShellActions = new Class({
	Implements: [Options, Events],
	options: {
		// onRun: $empty,
		// onClean: $empty,
		formId: 'show-result',
		saveAndReloadId: 'update',
		saveAsNewId: 'savenew',
		runId: 'run',
		cleanId: 'clean',
		entriesSelector: 'textarea',
		resultLabel: 'result_label',
		resultInput: 'select_link',
		exampleURL: '',
		exampleSaveURL: '',
		loadDependenciesURL: ''
	},
	/*
	 * Assign actions
	 */
	initialize: function(options) {
		this.setOptions(options);
		if ($(this.options.saveAndReloadId)) 
			$(this.options.saveAndReloadId).addEvent('click', this.saveAndReload.bind(this));
		if ($(this.options.saveAsNewId)) 
			$(this.options.saveAsNewId).addEvent('click', this.saveAsNew.bind(this));
		if ($(this.options.runId)) 
			$(this.options.runId).addEvent('click', this.run.bind(this));
		if ($(this.options.cleanId)) 
			$(this.options.cleanId).addEvent('click', this.cleanEntries.bind(this));
		// actions run if shell loaded
		
		this.form = document.id(this.options.formId);
		
		if (this.options.exampleURL) {
		//	this.run();
			this.displayExampleURL();
		}
	},
	// mark shell as favourite
	makeFavourite: function(shell_id) {
		new Request.JSON({
			'url': makefavouritepath,
			'data': {shell_id: shell_id},
			'onSuccess': function(response) {
				// #TODO: reload page after successful save
				$('mark_favourite').addClass('isFavourite')
					.getElements('span')[0].set('text', 'Base');
			}
		}).send();
	
	},
	// save and create new pastie
	saveAsNew: function() {
		Layout.updateFromMirror();
		$('id_slug').value='';
		$('id_version').value='0';
		new Request.JSON({
			'url': this.options.exampleSaveUrl,
			'onSuccess': function(json) {
				Layout.decodeEditors();
				if (!json.error) {
					// reload page after successful save
					window.location = json.pastie_url_relative; 
				} else {
					alert('ERROR: ' + json.error);
				}
			}
		}).send(this.form);
	},
	// update existing (create shell with new version)
	saveAndReload: function() {
		Layout.updateFromMirror();
		new Request.JSON({
			'url': this.options.exampleSaveUrl,
			'onSuccess': function(json) {
				// reload page after successful save
				Layout.decodeEditors();
				window.location = json.pastie_url_relative; 
			}
		}).send(this.form);
	},
	// run - submit the form (targets to the iframe)
	run: function() { 
		Layout.updateFromMirror();
		document.id(this.options.formId).submit();
		this.fireEvent('run');
	},
	// clean all entries, rename example to default value
	cleanEntries: function () {
		// here reload Mirrors
		Layout.cleanMirrors();
		$$(this.options.entriesSelector).each( function(t) {t.value='';});
		if (this.resultText) {
			document.id(this.options.resultLabel).set('text', this.resultText);
		}
		if ($(this.options.saveAndReloadId)) $(this.options.saveAndReloadId).destroy();
 		this.fireEvent('clean');
	},
	// rename iframe label to present the current URL
	displayExampleURL: function() {
		var resultInput = document.id(this.options.resultInput);
		if (resultInput) {
			if (Browser.Engine.gecko) {
				resultInput.setStyle('padding-top', '4px');
			}
			// resultInput.select();
		}
	},
	loadLibraryVersions: function(group_id) {
		new Request.JSON({
			url: this.options.loadLibraryVersionsURL.substitute({group_id: group_id}),
			onSuccess: function(response) {
				$('js_lib').empty();
				$('js_dependency').empty();
				response.libraries.each( function(lib) {
					new Element('option', {
						value: lib.id,
						text: "{group_name} {version}".substitute(lib)
					}).inject($('js_lib'));
					if (lib.selected) $('js_lib').set('value',lib.id);
				});
				response.dependencies.each(function (dep) {
					new Element('li', {
						html: [
							"<input id='dep_{id}' type='checkbox' name='js_dependency[{id}]' value='{id}'/>",
							"<label for='dep_{id}'>{name}</label>"
							].join('').substitute(dep)
					}).inject($('js_dependency'));
					if (dep.selected) $('dep_'+dep.id).set('checked', true);
				});
			}
		}).send();
	},
	loadDependencies: function(lib_id) {
		new Request.JSON({
			url: this.options.loadDependenciesURL.substitute({lib_id: lib_id}),
			onSuccess: function(response) {
				$('js_dependency').empty();
				response.each(function (dep) {
					new Element('li', {
						html: [
							"<input id='dep_{id}' type='checkbox' name='js_dependency[{id}]' value='{id}'/>",
							"<label for='dep_{id}'>{name}</label>"
							].join('').substitute(dep)
					}).inject($('js_dependency'));
					if (dep.selected) $('dep_'+dep.id).set('checked', true);
				});
			}
		}).send();
	}
});

/**
*
*  Base64 encode / decode
*  http://www.webtoolkit.info/
*
**/
 
var Base64 = {
 
	// private property
	_keyStr : "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
 
	// public method for encoding
	encode : function (input) {
		var output = "";
		input = input || "";
		var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
		var i = 0;
 
		input = Base64._utf8_encode(input);
 
		while (i < input.length) {
 
			chr1 = input.charCodeAt(i++);
			chr2 = input.charCodeAt(i++);
			chr3 = input.charCodeAt(i++);
 
			enc1 = chr1 >> 2;
			enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
			enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
			enc4 = chr3 & 63;
 
			if (isNaN(chr2)) {
				enc3 = enc4 = 64;
			} else if (isNaN(chr3)) {
				enc4 = 64;
			}
 
			output = output +
			this._keyStr.charAt(enc1) + this._keyStr.charAt(enc2) +
			this._keyStr.charAt(enc3) + this._keyStr.charAt(enc4);
 
		}
 
		return output;
	},
 
	// public method for decoding
	decode : function (input) {
		var output = "";
		var chr1, chr2, chr3;
		var enc1, enc2, enc3, enc4;
		var i = 0;
 
		input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
 
		while (i < input.length) {
 
			enc1 = this._keyStr.indexOf(input.charAt(i++));
			enc2 = this._keyStr.indexOf(input.charAt(i++));
			enc3 = this._keyStr.indexOf(input.charAt(i++));
			enc4 = this._keyStr.indexOf(input.charAt(i++));
 
			chr1 = (enc1 << 2) | (enc2 >> 4);
			chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
			chr3 = ((enc3 & 3) << 6) | enc4;
 
			output = output + String.fromCharCode(chr1);
 
			if (enc3 != 64) {
				output = output + String.fromCharCode(chr2);
			}
			if (enc4 != 64) {
				output = output + String.fromCharCode(chr3);
			}
 
		}
 
		output = Base64._utf8_decode(output);
 
		return output;
 
	},
 
	// private method for UTF-8 encoding
	_utf8_encode : function (string) {
		var utftext = "";
		string = string.replace(/\r\n/g,"\n");
 
		for (var n = 0; n < string.length; n++) {
 
			var c = string.charCodeAt(n);
 
			if (c < 128) {
				utftext += String.fromCharCode(c);
			}
			else if((c > 127) && (c < 2048)) {
				utftext += String.fromCharCode((c >> 6) | 192);
				utftext += String.fromCharCode((c & 63) | 128);
			}
			else {
				utftext += String.fromCharCode((c >> 12) | 224);
				utftext += String.fromCharCode(((c >> 6) & 63) | 128);
				utftext += String.fromCharCode((c & 63) | 128);
			}
 
		}
		return utftext;
	},
 
	// private method for UTF-8 decoding
	_utf8_decode : function (utftext) {
		var string = "";
		var i = 0;
		var c = c1 = c2 = 0;
 
		while ( i < utftext.length ) {
 
			c = utftext.charCodeAt(i);
 
			if (c < 128) {
				string += String.fromCharCode(c);
				i++;
			}
			else if((c > 191) && (c < 224)) {
				c2 = utftext.charCodeAt(i+1);
				string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
				i += 2;
			}
			else {
				c2 = utftext.charCodeAt(i+1);
				c3 = utftext.charCodeAt(i+2);
				string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
				i += 3;
			}
 
		}
 
		return string;
	}
 
}
