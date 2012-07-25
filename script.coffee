jQuery(document).ready ->
    writeanswer = (ans) ->
        jQuery("#answer").html(ans)
        
    answer = () ->
        question = jQuery("#question").val()
        jQuery.getJSON("/service/?question=#{question}", (data) -> writeanswer(data['answer']))
        
    jQuery("#ask").click( (event) ->
        event.preventDefault()
        answer() )
                        
    # Doesn't look like following is needed as firefox fires the
    # button click when enter pressed on the input field
    #jQuery("#question").keydown( (event) ->
        #if event.which == 13
            #answer() )
            
    # if the browser doesn't support svg, use a png
    if not document.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#BasicStructure", "1.1")
        jQuery("#robot").attr("src", "decisiverobot.png")