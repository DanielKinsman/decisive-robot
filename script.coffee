jQuery(document).ready ->
    writeanswer = (ans) ->
        jQuery("#answer").html(ans)
        jQuery("#answer").attr("class", "answered")
        jQuery(".unanswered").attr("class", "none")
        question = jQuery("#question").val()
        questionurl = "/?question=" + encodeURIComponent("#{question}")
        jQuery("#externallink").attr("href", questionurl)
        
    answer = () ->
        question = jQuery("#question").val()
        jQuery.getJSON("/service/?question=#{question}", (data) -> writeanswer(data['answer']))
            
    jQuery("form").submit( (event) ->
        event.preventDefault()
        answer()
        return false )
        
    #set focus to the question box
    jQuery("#question").focus()
            
    # if the browser doesn't support svg, replace svgs with pngs
    if not document.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#BasicStructure", "1.1")
        jQuery("#robot").attr("src", "decisiverobot.png")
        jQuery("#speechtick").attr("src", "speechtick.png")

	#if the browser is IE, tell them it is shit
	if jQuery.browser.msie
		alert("Decisive Robot works best on decent browsers like Firefox and Chrome. Don't use Internet Explorer, meatbag.")