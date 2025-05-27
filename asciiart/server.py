from concurrent import futures
import grpc
import asciiart_pb2
import asciiart_pb2_grpc
from pyfiglet import Figlet

class AsciiArtServicer(asciiart_pb2_grpc.AsciiArtServiceServicer):
    def __init__(self):
        self.fig = Figlet()
        self.available_styles = self.fig.getFonts()
    
    def GenerateArt(self, request, context):
        try:
            self.fig.setFont(font=request.style)
            art = self.fig.renderText(request.text)
            return asciiart_pb2.ArtResponse(art=art)
        except:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Invalid style selected")
            return asciiart_pb2.ArtResponse()
    
    def GetArtStyles(self, request, context):
        return asciiart_pb2.StyleResponse(styles=self.available_styles)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    asciiart_pb2_grpc.add_AsciiArtServiceServicer_to_server(
        AsciiArtServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("ASCII Art Server running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
