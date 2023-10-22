from queue import Queue
from script_query_service import QueryService
from script_yolo_service import YoloService
import detect_queue

def main(opt):
    req_queue = Queue(1)
    resp_queue = Queue(1)
    producer = QueryService('QueryImagePopupService', req_queue, resp_queue, False, opt['source'])
    consumer = YoloService('YoloDetectPopupService', req_queue, resp_queue, True, opt)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print('All threads terminate!')

if __name__ == '__main__':
    opt = detect_queue.parse_opt()   # <class 'argparse.Namespace'>
    main(vars(opt))
