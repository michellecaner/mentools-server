"""View module for handling requests about tools"""
from rest_framework.viewsets  import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from mentoolsapi.models import Tool

class ToolView(ViewSet):
    """Mentools tools view"""

    def retrieve(self, request, pk):
        """Handle a GET request for a tool"""
        tool =  Tool.objects.get(pk=pk)
        serializer = ToolSerializer(tool)
        return Response(serializer.data)

    def list(self, request):
        """Handle a GET request for all of the tools"""
        tools = Tool.objects.all()

        tool_type = request.query_params.get('type', None)
        if tool_type is not None:
            tools = tools.filter(tool_type_id=tool_type)

        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized tool instance
        """
        # if I had a customer/user field on my Tool model, I could use what's below to authenticate, but i don't
        
        # customer = Customer.objects.get(user=request.auth.user)

        new_tool = Tool.objects.create(
            # these are keyword arguments aka kwargs
            # request.data is the body that's coming in & is a dictionary
            title=request.data["title"],
            description=request.data["description"],
            tool_type=request.data["tool_type"],
            # customer=customer
        )
        serializer = ToolSerializer(new_tool)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handles PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        edited_tool = Tool.objects.get(pk=pk)
        edited_tool.title = request.data["title"]
        edited_tool.description = request.data["description"]
        edited_tool.tool_type = request.data["tool_type"]

        edited_tool.save()

        return Response(None,status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        tool = Tool.objects.get(pk=pk)
        tool.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ToolSerializer(serializers.ModelSerializer):
    """JSON serializer for tools"""

    class Meta:
        model =  Tool
        fields = ('id', 'title', 'description', 'tool_type')