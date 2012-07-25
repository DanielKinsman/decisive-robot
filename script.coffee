jQuery(document).ready ->
    writeanswer = (ans) ->
        jQuery("#answer").html(ans)
        jQuery("#answer").attr("class", "answered")
        jQuery(".unanswered").attr("class", "none")
        question = jQuery("#question").val()
        jQuery("#externallink").attr("href", "http://decisiverobot.com/?question=#{question}")
        
    answer = () ->
        question = jQuery("#question").val()
        jQuery.getJSON("/service/?question=#{question}", (data) -> writeanswer(data['answer']))
            
    jQuery("form").submit( (event) ->
        event.preventDefault()
        answer()
        return false )
        
    #set focus to the question box
    jQuery("#question").focus()
            
    # if the browser doesn't support svg, use a png
    if not document.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#BasicStructure", "1.1")
        jQuery("#robot").attr("src", "decisiverobot.png")